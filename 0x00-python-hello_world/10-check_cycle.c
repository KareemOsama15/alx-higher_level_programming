#include "lists.h"

/**
 * check_cycle - function checks if a singly linked list
 *    has  a cycle in it
 *
 * @list: head of Linked List
 * Return: 0 if no cycle , 1 if there a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr1 = list, *ptr2 = list;

	while (ptr1 && ptr2 && ptr2->next)
	{
		ptr1 = ptr1->next;
		ptr2 = ptr2->next->next;
		if (ptr1 == ptr2)
			return (1);
	}
	return (0);
}
