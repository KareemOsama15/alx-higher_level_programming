#include "lists.h"

/**
 * singlyLinkedList_size - get singly linked list size
 * @head: pointer to head of list
 * Return: number of nodes
 */
int singlyLinkedList_size(struct listint_s *head)
{
	listint_t *current = head;
	int count = 0;

	while (current)
	{
		count++;
		current = current->next;
	}
	return (count);
}

/**
 * linkedList_reverse - reversed all elements of linked list
 * @currentElement: pointer to head of list
 * Return: pointer to the reversed list
 */
listint_t *linkedList_reverse(struct listint_s **currentElement)
{
	listint_t *nextElement = (*currentElement)->next;
	listint_t *temp = *currentElement;
	listint_t *previous = NULL;

	while (temp)
	{
		previous = temp;
		temp = nextElement;
		if (nextElement)
			nextElement = nextElement->next;
		if (temp)
			temp->next = previous;
	}
	(*currentElement)->next = NULL;
	*currentElement = previous;
	return (*currentElement);
}

/**
 * is_palindrome - checks if linked list is a palindrome
 * @head: pointer to head of list
 * Return: 1 if palindrome, else 0
 */
int is_palindrome(listint_t **head)
{
	listint_t *mainList = *head, *reversedList = *head;
	int count, i = 0, j = 0;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	if ((*head)->next->next == NULL)
	{
		if ((*head)->n == (*head)->next->n)
			return (1);
		else
			return (0);
	}

	count = singlyLinkedList_size(*head);
	while (i < count / 2)
	{
		reversedList = reversedList->next;
		i++;
	}
	if (count % 2 != 0)
		count--;

	reversedList = reversedList->next;
	reversedList = linkedList_reverse(&reversedList);

	while (mainList && reversedList && j < count / 2)
	{
		if (mainList->n == reversedList->n)
		{
			mainList = mainList->next;
			reversedList = reversedList->next;
		}
		else
			return (0);
		j++;
	}
	return (1);
}
