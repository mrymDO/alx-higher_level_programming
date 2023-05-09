#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

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
		printf("%d\n", current->n);
		current = current->next;
		i++;
	}

	return (i);
}

/**
 * add_nodeint_end - Adds a new node at the end of a list
 * @head: a pointer to a pointer to the head of the list
 * @n: value stored in node
 * Return: a pointer to the new node, NULL if it failed
 */

listint_t *add_nodeint_end(listint_t **head, const int n)
{
	listint_t *current;
	listint_t *new_node;

	if (head == NULL)
		return (NULL);

	new_node = malloc(sizeof(listint_t));

	if (new_node == NULL)
		return (NULL);

	new_node->n = n;
	new_node->next = NULL;

	if (*head == NULL)
	{
		*head = new_node;
		return (new_node);
	}

	current = *head;
	while (current->next != NULL)
	{
		current = current->next;
	}

	current->next = new_node;

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
