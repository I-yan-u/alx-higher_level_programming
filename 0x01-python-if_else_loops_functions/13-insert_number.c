#include "lists.h"

/**
 * insert_node - Inserts node in sorted list
 * @head: The pointer to the head of the list
 * @number: Number to be added to list
 * 
 * Return: pointer t the new node
 */

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new;
    listint_t *current;

    current = *head;

    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);

    new->n = number;
    new->next = NULL;

    if (current == NULL || current->n >= number)
    {
        new->next = current;
        *head = new;
        return (new);
    }
     else
    {
        while (current->next && current->next->n < new->n )
            current = current->next;

        new->next = current->next;
        current->next = new;
    }
    return (new);
}
