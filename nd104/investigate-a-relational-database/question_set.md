# Question Set 1
## Question 1
We want to understand more about the movies that families are watching. The following categories are considered family movies: Animation, Children, Classics, Comedy, Family and Music.

```sql
WITH family_categories AS (
    SELECT category_id, name
    FROM category
    WHERE name IN ('Animation', 'Children', 'Classics', 'Comedy', 'Family', 'Music')
)
SELECT 
  f.title AS film_title,
  c.name AS category_name,
  COUNT(r.rental_id) AS rental_count
FROM rental r
INNER JOIN inventory i ON r.inventory_id = i.inventory_id
INNER JOIN film f ON f.film_id = i.film_id
INNER JOIN film_category fc ON fc.film_id = f.film_id
INNER JOIN family_categories c ON fc.category_id = c.category_id
GROUP BY f.title, c.name
ORDER BY category_name, film_title;
```

## Question 2
Now we need to know how the length of rental duration of these family-friendly movies compares to the duration that all movies are rented for. Can you provide a table with the movie titles and divide them into 4 levels (first_quarter, second_quarter, third_quarter, and final_quarter) based on the quartiles (25%, 50%, 75%) of the average rental duration(in the number of days) for movies across all categories? Make sure to also indicate the category that these family-friendly movies fall into.

```sql
SELECT 
  f.title, c.name, f.rental_duration,
  NTILE(4) OVER (ORDER BY f.rental_duration) AS standard_quartile
FROM film f
JOIN film_category fc
ON f.film_id = fc.film_id
JOIN (
    SELECT category_id, name
    FROM category
    WHERE name IN ('Animation', 'Children', 'Classics', 'Comedy', 'Family', 'Music')) AS c
ON fc.category_id = c.category_id;
```

## Question 3
Finally, provide a table with the family-friendly film category, each of the quartiles, and the corresponding count of movies within each combination of film category for each corresponding rental duration category. The resulting table should have three columns:

* Category
* Rental length category
* Count

```sql
WITH family_films AS (
    SELECT 
      f.title, c.name AS category, f.rental_duration,
      NTILE(4) OVER (ORDER BY f.rental_duration) AS standard_quartile
    FROM film f
    INNER JOIN film_category fc ON f.film_id = fc.film_id
    INNER JOIN category c ON fc.category_id = c.category_id
    WHERE c.name IN ('Animation', 'Children', 'Classics', 'Comedy', 'Family', 'Music')
)
SELECT category, standard_quartile, COUNT(*)
FROM family_films
GROUP BY category, standard_quartile
ORDER BY category, standard_quartile;
```

# Question Set 2
## Question 1
We want to find out how the two stores compare in their count of rental orders during every month for all the years we have data for. Write a query that returns the store ID for the store, the year and month and the number of rental orders each store has fulfilled for that month. Your table should include a column for each of the following: year, month, store ID and count of rental orders fulfilled during that month.

```sql
SELECT
  DATE_TRUNC('month', rental_date) AS pay_mon,
  i.store_id,
  COUNT(*) AS count_rentals
FROM rental r
INNER JOIN inventory i ON r.inventory_id = i.inventory_id
GROUP BY pay_mon, i.store_id
ORDER BY pay_mon;
```

## Question 2
We would like to know who were our top 10 paying customers, how many payments they made on a monthly basis during 2007, and what was the amount of the monthly payments. Can you write a query to capture the customer name, month and year of payment, and total payment amount for each month by these top 10 paying customers?

```sql
WITH top_customers AS (
  SELECT c.customer_id,
  c.first_name || ' ' || c.last_name AS full_name,
  SUM(p.amount) AS total_amount
  FROM payment p
  INNER JOIN customer c ON p.customer_id = c.customer_id
  GROUP BY c.customer_id, full_name
  ORDER BY total_amount DESC
  LIMIT 10
)

SELECT 
  DATE_TRUNC('month', p.payment_date) AS pay_mon,
  tc.full_name,
  COUNT(p.amount) AS pay_countermon,
  SUM(p.amount) AS pay_amount
FROM payment p
INNER JOIN top_customers tc ON p.customer_id = tc.customer_id
GROUP BY pay_mon, tc.full_name
ORDER BY tc.full_name, pay_mon;
```

## Question 3

Finally, for each of these top 10 paying customers, I would like to find out the difference across their monthly payments during 2007. Please go ahead and write a query to compare the payment amounts in each successive month. Repeat this for each of these 10 paying customers. Also, it will be tremendously helpful if you can identify the customer name who paid the most difference in terms of payments.

```sql
WITH top_customers AS (
  SELECT 
    c.customer_id,
    c.first_name || ' ' || c.last_name AS full_name,
    SUM(p.amount) AS total_amount
  FROM payment p
  INNER JOIN customer c ON p.customer_id = c.customer_id
  GROUP BY c.customer_id, full_name
  ORDER BY total_amount DESC
  LIMIT 10),
pay_per_month AS (
  SELECT 
    DATE_TRUNC('month', p.payment_date) AS pay_mon,
    tc.full_name,
    COUNT(p.amount) AS pay_countermon,
    SUM(p.amount) AS pay_amount
  FROM payment p
  INNER JOIN top_customers tc ON p.customer_id = tc.customer_id
  GROUP BY pay_mon, tc.full_name
  ORDER BY tc.full_name, pay_mon)
SELECT 
  pay_mon, full_name, pay_countermon, pay_amount,
  COALESCE(pay_amount - LAG(pay_amount) OVER (PARTITION BY full_name ORDER BY pay_mon), 0) AS diff
FROM pay_per_month
WHERE pay_mon > '2007-01-01';
```

```sql
WITH top_customers AS (
  SELECT 
    c.customer_id,
    c.first_name || ' ' || c.last_name AS full_name,
    SUM(p.amount) AS total_amount
  FROM payment p
  INNER JOIN customer c ON p.customer_id = c.customer_id
  GROUP BY c.customer_id, full_name
  ORDER BY total_amount DESC
  LIMIT 10),
pay_per_month AS (
  SELECT 
    DATE_TRUNC('month', p.payment_date) AS pay_mon,
    tc.full_name,
    COUNT(p.amount) AS pay_countermon,
    SUM(p.amount) AS pay_amount
  FROM payment p
  INNER JOIN top_customers tc ON p.customer_id = tc.customer_id
  GROUP BY pay_mon, tc.full_name
  ORDER BY tc.full_name, pay_mon)
SELECT 
  pay_mon, full_name, pay_countermon, pay_amount,
  COALESCE(pay_amount - LAG(pay_amount) OVER (PARTITION BY full_name ORDER BY pay_mon), 0) AS diff
FROM pay_per_month
ORDER BY diff DESC
LIMIT 1;
```

# Question Set 3
## Question 1
I'm interested in identifying actors who excel in family-friendly movies. Could you please provide the top 10 actors based on the highest number of movie rentals across all family-friendly films?

```sql
SELECT f.film_id, f.title
FROM film f
JOIN film_category fc
ON f.film_id = fc.film_id
JOIN category c
ON fc.category_id = c.category_id
WHERE c.name IN ('Animation', 'Children', 'Classics', 'Comedy', 'Family', 'Music')
```


```sql
WITH family_films AS (
    SELECT f.film_id, f.title
    FROM film f
    JOIN film_category fc
    ON f.film_id = fc.film_id
    JOIN category c
    ON fc.category_id = c.category_id
    WHERE c.name IN ('Animation', 'Children', 'Classics', 'Comedy', 'Family', 'Music')
    )

SELECT a.actor_id, a.first_name || ' ' || a.last_name AS full_name, COUNT(r.rental_id) AS rental_count
FROM family_films
JOIN film_actor fa
ON family_films.film_id = fa.film_id
JOIN actor a
ON fa.actor_id = a.actor_id
JOIN inventory i
ON family_films.film_id = i.film_id
JOIN rental r
ON i.inventory_id = r.inventory_id
GROUP BY a.actor_id, full_name
ORDER BY rental_count DESC
LIMIT 10;
```

## Question 2
I'm interested in discovering which actors excel in family-friendly movies. Could we analyze the monthly rental trends for the top 5 actors with the highest number of movie rentals across all family-friendly genres?

```sql
WITH family_films AS (
    SELECT f.film_id, f.title
    FROM film f
    INNER JOIN film_category fc
    ON f.film_id = fc.film_id
    INNER JOIN category c
    ON fc.category_id = c.category_id
    WHERE c.name IN ('Animation', 'Children', 'Classics', 'Comedy', 'Family', 'Music')
    ),
top_actors AS (
    SELECT a.actor_id
    FROM family_films
    INNER JOIN film_actor fa
    ON family_films.film_id = fa.film_id
    INNER JOIN actor a
    ON fa.actor_id = a.actor_id
    INNER JOIN inventory i
    ON family_films.film_id = i.film_id
    INNER JOIN rental r
    ON i.inventory_id = r.inventory_id
    GROUP BY a.actor_id
    ORDER BY COUNT(r.rental_id) DESC
    LIMIT 5
    )
SELECT 
  DATE_TRUNC('month', r.rental_date) AS pay_mon,
  a.first_name || ' ' || a.last_name AS full_name,
  COUNT(r.rental_id) AS rental_count
FROM family_films
INNER JOIN film_actor fa
ON family_films.film_id = fa.film_id
INNER JOIN actor a
ON fa.actor_id = a.actor_id
INNER JOIN inventory i
ON family_films.film_id = i.film_id
INNER JOIN rental r
ON i.inventory_id = r.inventory_id
WHERE EXISTS (SELECT 1 FROM top_actors ta WHERE ta.actor_id = a.actor_id)
GROUP BY pay_mon, full_name
ORDER BY full_name, pay_mon
```