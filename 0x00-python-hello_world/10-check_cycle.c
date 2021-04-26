#include "lists.h"

/**
 * check_cycle - checks list has a loop
 * @list: pointer
 * Return: 1 loop, 0 if no is loop
 */

int check_cycle(listint_t *list)
{
	listint_t *fast = list;

	if (!list)
		return (0);
	while (list && fast && fast->next)
	{
		fast = fast->next->next;
		list = list->next;
		if (list == fast)
			return (1);
	}
	return (0);
}
