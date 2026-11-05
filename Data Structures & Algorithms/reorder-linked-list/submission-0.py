
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        # 1. Encontrar la mitad
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Separar las listas
        curr = slow.next
        slow.next = None
        prev = None

        # 3. Invertir la segunda mitad
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # 4. Intercalar las dos listas
        first = head
        second = prev

        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2
