from typing import List, Optional

class RouteTrieNode:
    def __init__(self):
        self.children = {}
        self.handler = None

class RouteTrie:
    def __init__(self, root_handler: str):
        self.root = RouteTrieNode()
        self.root.handler = root_handler

    def insert(self, path_parts: List[str], handler: str) -> None:
        current_node = self.root
        for part in path_parts:
            if part not in current_node.children:
                current_node.children[part] = RouteTrieNode()
            current_node = current_node.children[part]
        current_node.handler = handler

    def find(self, path_parts: List[str]) -> Optional[str]:
        current_node = self.root
        for part in path_parts:
            if part in current_node.children:
                current_node = current_node.children[part]
            else:
                return None
        return current_node.handler

class Router:
    def __init__(self, root_handler: str, not_found_handler: str):
        self.route_trie = RouteTrie(root_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, path: str, handler: str) -> None:
        path_parts = self.split_path(path)
        self.route_trie.insert(path_parts, handler)

    def lookup(self, path: str) -> str:
        path_parts = self.split_path(path)
        handler = self.route_trie.find(path_parts)
        return handler if handler else self.not_found_handler

    def split_path(self, path: str) -> List[str]:
        # Split the path into parts and remove empty parts to handle trailing slashes
        return [part for part in path.split('/') if part]
    
if __name__ == '__main__':
    # create the router and add a route
    router = Router("root handler", "not found handler")
    router.add_handler("/home/about", "about handler")

    # Edge case: Empty path
    print(router.lookup(""))
    # Expected output: 'not found handler'

    # Edge case: Root path with trailing slash
    print(router.lookup("/"))
    # Expected output: 'root handler'

    # Edge case: Path with multiple trailing slashes
    print(router.lookup("/home/about//"))
    # Expected output: 'about handler'

    # Normal case: Path not found
    print(router.lookup("/home/contact"))
    # Expected output: 'not found handler'

    # Normal case: Path with multiple segments
    print(router.lookup("/home/about/me"))
    # Expected output: 'not found handler'

    # Normal case: Path with exact match
    print(router.lookup("/home/about"))
    # Expected output: 'about handler'