#include "lists.h"
#include <stdio.h>


/**
 * print_listint - prints all elements of listint_t list
 * @h: pointer to the head of the list
 * Return: number of nodes
 */

size_t print_listint(const listint_t *h)
{
	unsigned int i = 0;
	const listint_t *current = h;

	if (current == NULL)
		return (0);

	while (current != NULL)
	{
		printf("%i\n", current->n);
		current = current->next;
		i++;
	}

	return (i);
}



/**
 * add_nodeint - adds a new node at the begining of a listint_t list
 * @head: Pointer to a pointer the head node of the linked list
 * @n: value to be stored in the new node
 * Return:  Adress of the new node, or NULL
 */

listint_t *add_nodeint(listint_t **head, const int n)
{
	listint_t *new_node;

	new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);

	new_node->n = n;
	new_node->next = *head;
	*head = new_node;

	return (new_node);
}

/**
 * free_listint - Frees a listint_t list
 * @head: pointer to the head of the list
 */

void free_listint(listint_t *head)
{
	listint_t *current;

	if (head == NULL)
		return;

	while (head != NULL)
	{
		current = head;
		head = head->next;
		free(current);
	}
}
