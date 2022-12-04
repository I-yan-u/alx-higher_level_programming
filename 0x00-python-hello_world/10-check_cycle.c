#include "lists.h"

/**
 * check_cycle - Checks if a  linked list has a cycle.
 * @h: The pointer to the first node.
 *
 * Return: Returns 1 if true, Returns 0 if false.
 */

int check_cycle(listint_t *h)
{
    listint_t *t1node, *t2node;
    unsigned int n = 1;

    t1node = h;
    t2node = h;
    
    while(n != 0 && t2node != NULL)
    {
        t1node = t1node->next;
        t2node = t2node->next->next;
        if(t1node == t2node)
        {
            return (1);
        }
    }
    return (0);
}
