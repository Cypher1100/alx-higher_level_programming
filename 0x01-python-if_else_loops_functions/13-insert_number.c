#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: pointer to the head node
 * @number: The number to be inseted
 * Return: Null if fail and a pointer to the new node if success
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *newnode;

	newnode = malloc(sizeof(listint_t));
	if (newnode == NULL)
		return NULL;
	newnode->n = number;

	if (node == NULL || node->n >=number)
	{
		newnode->next = node;
		*head = newnode;
		return (new);
	}
	while (node && node->next && node->next->n < number)
		node = node->next;

	newnode->next = node->next;
	node->next = newnode;

	return newnode;
