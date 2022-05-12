def has_cycle(head):
    back = head
    front = head
    while front and front.next:
        back = back.next
        front = front.next.next
        if back == front:
            return 1
    return 0
