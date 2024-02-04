# Question Set 1
## Question 1
We want to understand more about the movies that families are watching. The following categories are considered family movies: Animation, Children, Classics, Comedy, Family and Music.

```sql
SELECT 
f.title AS film_title,
c.name AS category_name,
sub1.rental_count
FROM (
	SELECT f.film_id, COUNT(r.rental_id) AS rental_count
	FROM rental r
	JOIN inventory i
	ON r.inventory_id = i.inventory_id
	JOIN film f
	ON f.film_id = i.film_id
	GROUP BY 1) AS sub1
JOIN film AS f
ON sub1.film_id = f.film_id
JOIN film_category fc
ON fc.film_id = f.film_id
JOIN (
	SELECT *
    FROM category c
	WHERE c.name IN ('Animation', 'Children', 'Classics', 'Comedy', 'Family', 'Music')) AS c
ON fc.category_id = c.category_id
ORDER BY 2, 1;
```

## Question 2
Now we need to know how the length of rental duration of these family-friendly movies compares to the duration that all movies are rented for. Can you provide a table with the movie titles and divide them into 4 levels (first_quarter, second_quarter, third_quarter, and final_quarter) based on the quartiles (25%, 50%, 75%) of the average rental duration(in the number of days) for movies across all categories? Make sure to also indicate the category that these family-friendly movies fall into.

```sql
SELECT f.title, c.name, f.rental_duration,
NTILE(4) OVER (ORDER BY rental_duration) AS standard_qurtile
FROM film f
JOIN film_category fc
ON f.film_id = fc.film_id
JOIN category c
ON fc.category_id = c.category_id
WHERE c.name IN ('Animation', 'Children', 'Classics', 'Comedy', 'Family', 'Music');
```

## Question 3
Finally, provide a table with the family-friendly film category, each of the quartiles, and the corresponding count of movies within each combination of film category for each corresponding rental duration category. The resulting table should have three columns:

* Category
* Rental length category
* Count

```sql
SELECT sub1.name, sub1.standard_qurtile, COUNT(*)
FROM (
	SELECT f.title, c.name, f.rental_duration,
	NTILE(4) OVER (ORDER BY rental_duration) AS standard_qurtile
	FROM film f
	JOIN film_category fc
	ON f.film_id = fc.film_id
	JOIN category c
	ON fc.category_id = c.category_id
	WHERE c.name IN ('Animation', 'Children', 'Classics', 'Comedy', 'Family', 'Music')) sub1
GROUP BY 1, 2
ORDER BY 1, 2;
```

# Question Set 2

## Question 1
We want to find out how the two stores compare in their count of rental orders during every month for all the years we have data for. Write a query that returns the store ID for the store, the year and month and the number of rental orders each store has fulfilled for that month. Your table should include a column for each of the following: year, month, store ID and count of rental orders fulfilled during that month.

```sql
SELECT
CAST(SUBSTR(CAST(rental_date AS text), 6, 2) AS INT) AS rental_month,
CAST(SUBSTR(CAST(rental_date AS text), 1, 4) AS INT) AS rental_year,
store_id,
COUNT(*) AS count_rentals
FROM rental r
JOIN inventory i
ON r.inventory_id = i.inventory_id
GROUP BY 1, 2, 3
ORDER BY 2, 1;
```

## Question 2
We would like to know who were our top 10 paying customers, how many payments they made on a monthly basis during 2007, and what was the amount of the monthly payments. Can you write a query to capture the customer name, month and year of payment, and total payment amount for each month by these top 10 paying customers?

```sql
WITH top_customers AS (
  SELECT c.customer_id,
  c.first_name || ' ' || c.last_name AS full_name,
  SUM(p.amount) AS total_amount
  FROM payment p
  JOIN customer c ON p.customer_id = c.customer_id
  GROUP BY c.customer_id, full_name
  ORDER BY total_amount DESC
  LIMIT 10
)

SELECT DATE_TRUNC('month', p.payment_date) AS pay_mon,
tc.full_name,
COUNT(p.amount) AS pay_countermon,
SUM(p.amount) AS pay_amount
FROM payment p
JOIN top_customers tc ON p.customer_id = tc.customer_id
GROUP BY pay_mon, tc.full_name
ORDER BY tc.full_name, pay_mon;
```

## Question 3

Finally, for each of these top 10 paying customers, I would like to find out the difference across their monthly payments during 2007. Please go ahead and write a query to compare the payment amounts in each successive month. Repeat this for each of these 10 paying customers. Also, it will be tremendously helpful if you can identify the customer name who paid the most difference in terms of payments.

```sql
WITH top_customers AS (
  SELECT c.customer_id,
  c.first_name || ' ' || c.last_name AS full_name,
  SUM(p.amount) AS total_amount
  FROM payment p
  JOIN customer c ON p.customer_id = c.customer_id
  GROUP BY c.customer_id, full_name
  ORDER BY total_amount DESC
  LIMIT 10),
pay_per_month AS (
  SELECT DATE_TRUNC('month', p.payment_date) AS pay_mon,
  tc.full_name,
  COUNT(p.amount) AS pay_countermon,
  SUM(p.amount) AS pay_amount
  FROM payment p
  JOIN top_customers tc ON p.customer_id = tc.customer_id
  GROUP BY pay_mon, tc.full_name
  ORDER BY tc.full_name, pay_mon)
SELECT pay_mon, full_name, pay_countermon, pay_amount,
LEAD(pay_amount) OVER (PARTITION BY full_name ORDER BY pay_mon) - pay_amount AS diff
FROM pay_per_month
```

```sql
WITH top_customers AS (
  SELECT c.customer_id,
  c.first_name || ' ' || c.last_name AS full_name,
  SUM(p.amount) AS total_amount
  FROM payment p
  JOIN customer c ON p.customer_id = c.customer_id
  GROUP BY c.customer_id, full_name
  ORDER BY total_amount DESC
  LIMIT 10),
pay_per_month AS (
  SELECT DATE_TRUNC('month', p.payment_date) AS pay_mon,
  tc.full_name,
  COUNT(p.amount) AS pay_countermon,
  SUM(p.amount) AS pay_amount
  FROM payment p
  JOIN top_customers tc ON p.customer_id = tc.customer_id
  GROUP BY pay_mon, tc.full_name
  ORDER BY tc.full_name, pay_mon)
SELECT pay_mon, full_name, pay_countermon, pay_amount,
COALESCE(LEAD(pay_amount) OVER (PARTITION BY full_name ORDER BY pay_mon) - pay_amount, 0) AS diff
FROM pay_per_month
ORDER BY diff DESC
LIMIT 1;
```