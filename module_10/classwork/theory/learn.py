# from dataclasses import dataclass
# from typing import Any, Optional
# # односвязанный список

# @dataclass
# class Node:
#     value: Any
#     next: Optional[Node] = None

# c = Node("C")
# b = Node("B", next=c)
# a = Node("A", next=b)

# print(a)
# print(a.next)
# print(a.next.next)

# def print_list(head: Optional[Node]) -> None:
#     current= head
#     while current is not None:
#         print(current.value, end=" -> ")
#         current = current.next
#     print("None")
# print_list(a)


# from dataclasses import dataclass
# from typing import Any, Optional
# # двусвязный список

# @dataclass
# class DoubleNode:
#     value: Any
#     next: Optional["DoubleNode"] = None
#     prev: Optional["DoubleNode"] = None

# a = DoubleNode("page1")
# b = DoubleNode("page2")
# c = DoubleNode("page3")

# a.next= b
# b.prev= a
# b.next= c
# c.prev= b

# print(c.prev.value)
# print(b.prev.value, "<->", b.value, "<->", b.next.value)



# from dataclasses import dataclass
# from typing import Any, Optional
# from collections import deque
# from heapq import heappush, heappop

# # Очередь

# queue = deque()
# queue.append("A")
# queue.append("B")
# queue.append("C")

# print("очередь: ", queue)
# print("выполнили:", queue.popleft())
# print("после выполнения:", queue)


# from dataclasses import dataclass
# from typing import Any, Optional
# from collections import deque
# from heapq import heappush, heappop

# priority_queue= []
# heappush(priority_queue, (3, "C"))
# heappush(priority_queue, (1, "A"))
# heappush(priority_queue, (2, "B"))

# while priority_queue:
#     property_n, task = heappop(priority_queue)
#     print(property_n, task)



from dataclasses import dataclass
from typing import Any, Optional
from collections import deque
from heapq import heappush, heappop

@dataclass
class TreeNode:
    value: Any
    left: Optional["TreeNode"] = None
    right: Optional["TreeNode"] = None

root = TreeNode(
    "A", 
    left=TreeNode(
        "B",
        left=TreeNode("D"),
        right=TreeNode("E")
        ),
        right=TreeNode(
            "C",
            left=TreeNode("F")
        )
)

def preorder(node: Optional[TreeNode]) -> None:
    if node is None:
        return
    print(node.value)
    preorder(node.left)
    preorder(node.right)

print("Обход")
preorder(root)