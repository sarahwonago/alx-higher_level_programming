#include "lists.h"

/**
 * int check_cycle(listint_t *list) - checks for
 * a cycle
 *
 * @list: the singly linked list
 * Return: 1 if cycle else 0
 */
int check_cycle(listint_t *list)
{
	listint_t *one, *two;

	if (!list || !list->next)
		return (0);

	one = list;
	two = list;

	while (two != NULL && one != NULL && one->next != NULL)
	{
		two = two->next;
		one = one->next->next;
		if (one == two)
		{
			return (1);
		}
	}

	return (0);
}
