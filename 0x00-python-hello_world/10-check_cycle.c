#include "lists.h"

/**
 * check_cycle - checks whether its a circular list
 * @head: pointer to the start of the list
 * Return: 0 if no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *current;

	current = list;
	while (1)
	{
		current = current->next;
		if (current == NULL)
		{
			return (0);
		}
		else if (current == list)
		{
			return (1);
		}
	}
}
