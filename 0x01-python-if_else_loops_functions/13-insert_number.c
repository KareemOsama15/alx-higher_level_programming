#include "lists.h"

/**
 * insert_node - function checks if a singly linked list
 *    has  a cycle in it
 *
 * @head: head of Linked List
 * @number: number
 * Return: address of new node, or NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *newElement = NULL, *current = *head;

	if (!*head)
		return (NULL);
	newElement = (struct listint_s *)malloc(sizeof(struct listint_s));
	if (!newElement)
		return (NULL);

	newElement->n = number;
	if (current->n >= newElement->n)
	{
		newElement->next = *head;
		*head = newElement;
		return (newElement);
	}
	while (current)
	{
		/* 1 2 3 4 -27- 98 402 1024 */
		if (current->next != NULL && current->next->n >= newElement->n)
		{
			newElement->next = current->next;
			current->next = newElement;
			return (newElement);
		}
		else if (current->next == NULL)
		{
			newElement->next = NULL;
			current->next = newElement;
			return (newElement);
		}
		current = current->next;
	}
	return (NULL);
}
