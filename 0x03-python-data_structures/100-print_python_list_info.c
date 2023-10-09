#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - function
 *
 * @p: python object that prints some basic info
 *		about Python lists
 *
 * Return: no return
 */
void print_python_list_info(PyObject *p)
{
	size_t i = 0, length;
	PyListObject *list;
	PyObject *item;

	length = Py_SIZE(p);
	printf("[*] Size of the Python List = %ld\n", length);

	list = (PyListObject *)p;
	printf("[*] Allocated = %ld\n", list->allocated);

	while (i < length)
	{
		item = PyList_GetItem(p, i);
		printf("Element [i]: %s\n", Py_TYPE(item)->tp_name);
		i++;
	}
}
