#include <stdio.h>
#include <Python.h>
#include <time.h>

/**
 * print_python_list_info - function
 *
 * @p: python object that prints some basic info
 *		about Python lists
 * Return: no return
 */
void print_python_list_info(PyObject *p)
{
	size_t length, i;
	int element;
	PyObject *item;

	length = Py_SIZE(p);
	printf("[*] Size of the Python List = %lu\n", length);

	element = ((PyListObject *)p)->allocated;
	printf("[*] Allocated = %d\n", element);

	for (i = 0; i < length; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %lu: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
