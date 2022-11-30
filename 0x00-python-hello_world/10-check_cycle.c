#include "lists.h"

/**
 * Check_cycle - checks if a singly linked list has a cycle in it.
 * @list
 *
 * Return: 1 if successful and 0 if fail
 */
int int check_cycle(listint_t *list)
{
	listint_t *peter = list;
	listint_t *paul = list;

	if (!list)
		return (0);
	while (peter && paul && paul->next)
	{
		peter = peter->next;
		paul = paul->next->next;
		if (peter == paul)
			return 1;
	}
	return 0;
