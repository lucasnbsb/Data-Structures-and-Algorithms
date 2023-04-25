func deleteDuplicates(head *ListNode) *ListNode {
	anchor := head

	for head != nil {
		if head.Next != nil && head.Val == head.Next.Val {
			head.Next = head.Next.Next
		} else {
			head = head.Next
		}
	}

	return anchor
}