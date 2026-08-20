class Solution:
    def reverse(self, head: Optional[ListNode], times: int):
        curr = head
        prev = None

        while times:
            nex = curr.next
            curr.next = prev
            prev = curr
            curr = nex
            times -= 1

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head == None:
            return None

        left = head
        right = None
        res = None
        prevleft = None
        size = k

        while True:
            right = left

            for i in range(size - 1):
                if right == None:
                    break

                right = right.next

            if right:

                nextleft = right.next

                self.reverse(left, k)

                if prevleft:
                    prevleft.next = right

                prevleft = left

                if res == None:
                    res = right

                left = nextleft

            else:

                if prevleft:
                    prevleft.next = left

                if res == None:
                    res = left

                break

        return res