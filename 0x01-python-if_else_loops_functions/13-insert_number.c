#include "lists.h"

/**
 * insert_node - Number
 * @head: Head
 * @number: Count
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node, *new;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);
	node = *head;
	new->n = number;
	if (!*head || node->n > number)
		return (new->next = *head, *head = new, new);
	while (node->next)
	{
		if (node->next->n >= number)
			return (new->next = node->next, node->next = new, new);
		node = node->next;
	}
	new->next = NULL;
	node->next = new;
	return (new);
}
