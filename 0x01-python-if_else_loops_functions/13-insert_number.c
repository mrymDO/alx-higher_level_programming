#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - insert a number into a sorted singly linked list
 * @head: a pointer to a pointer to the head of the linked list
 * @number: value to be inserted
 * Return: a pointer to new node inserted or NULL on faillure
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current;

	if (head == NULL)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (*head == NULL)
	{
		*head = new;
		return (new);
	}

	if (number < (*head)->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	current = *head;
	while (current->next != NULL && current->next->n < number)
		current = current->next;

	if (current == NULL)
	{
		free(new);
		return (NULL);
	}

	new->next = current->next;
	current->next = new;

	return (new);
}
