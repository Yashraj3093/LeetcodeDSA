# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not k or not head: return head

        current = head
        arr = []
        while current:
            arr.append(current.val)
            current = current.next

        k = k % len(arr)
        arr = arr[-k:] + arr[:-k]

        current = head
        i = 0
        while current:
            current.val = arr[i]
            i += 1
            current = current.next

        return head