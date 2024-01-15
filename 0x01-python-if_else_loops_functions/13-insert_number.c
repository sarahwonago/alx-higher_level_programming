#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
#include <unistd.h>

/**
 * insert_node - insert an int into a list
 *
 * @head: linked list
 * @number: integer to be inserted
 *
 * Return: pointer to new head
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *c_pointer = *head;
	listint_t *new = NULL;
	listint_t *temp = NULL;

	if (!head)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number;
	new->next = NULL;

	if (!*head || (*head)->n > number)
	{
		new->next = *head;
		return (*head = new);
	}
	else
	{
		while (c_pointer && c_pointer->n < number)
		{
			temp = c_pointer;
			c_pointer = c_pointer->next;
		}

		temp->next = new;
		new->next = c_pointer;
	}

	return (new);
}
