package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func main() {
	inputSlice := []int{1, 2, 3, 3, 4, 4, 5}

	head := buildLinkedList(inputSlice)

	for head != nil {
		fmt.Println(head.Val)
		head = head.Next
	}
}

func buildLinkedList(arr []int) *ListNode {
	res := &ListNode{}
	anchor := res

	for i := range arr {
		newNode := ListNode{i, nil}
		res.Next = &newNode
		res = res.Next
	}

	return anchor.Next
}
