func countNodes(head *ListNode) int{
	 count := 0
	 for head != nil {
		 count++
		 head = head.Next
	 }
	 return count
 }
 
 func getMid(head *ListNode) *ListNode {
	 slow, fast := head, head
	 for fast.Next != nil && fast.Next.Next != nil {
		 fast = fast.Next.Next
		 slow = slow.Next
	 }
	 return slow
 }
 
 func mergeLists(l1 *ListNode, l2 *ListNode) *ListNode{
	 res := ListNode{}
	 cur := &res
 
	 for l1 != nil && l2 != nil {
		 if l1.Val < l2.Val{
			 cur.Next = l1
			 l1 = l1.Next
		 }else {
			 cur.Next = l2
			 l2 = l2.Next
		 }
		 cur = cur.Next
	 }
 
	 if l1 != nil{
		 cur.Next = l1
	 }else{
		 cur.Next = l2
	 }
 
	 return res.Next
 }
 
 
 func sortList(head *ListNode) *ListNode {
	 if head == nil || head.Next == nil {
		 return head
	 }
 
	 // split the list into two
	 left := head
	 right := getMid(head)
	 tmp := right.Next
	 right.Next = nil
	 right = tmp
 
	 left = sortList(left)
	 right = sortList(right)
	 return mergeLists(left, right)
 }