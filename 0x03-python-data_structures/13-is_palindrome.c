#include "lists.h"


/**
 * reverse_listint - reverses a listint_t linked list
 * @head: a pointer to a pointer to the head of linked list
 * Return: a pointer to the first node of the reversed list
 */

listint_t *reverse_listint(listint_t **head)
{
	listint_t *temp1 = NULL;
	listint_t *temp2 = NULL;

	if (*head == NULL)
		return (NULL);

	while (*head != NULL)
	{
		temp2 = (*head)->next;
		(*head)->next = temp1;
		temp1 = (*head);
		(*head) = temp2;
	}

	(*head) = temp1;

	return (*head);
}
/**
 * is_palindrome - checks if a singly linked list is a palindrome
 * @head: a pointer to a pointer to the head of the linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *first = *head, *last = *head;
	listint_t *mid;

	if (*head == NULL)
		return (1);

	while (last != NULL && last->next != NULL)
	{
		first = first->next;
		last = last->next->next;
	}
	first->next = reverse_listint(&(first->next));
	mid = first->next;
	while (mid != NULL)
	{
		if (mid->n != (*head)->n)
			return (0);
		*head = (*head)->next;
		mid = mid->next;
	}
	return (1);
}
