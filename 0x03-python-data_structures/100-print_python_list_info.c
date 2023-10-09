#include <stdio.h>
#include <Python.h>

void print_python_list_info(PyObject *p)
{
    size_t i = 0, length;
    PyObject *item;

    if (!p)
    {
        printf("[*] Size of the Python List = 0\n");
        printf("[*] Allocated = 0\n");
    }
    else
    {
        length = PyList_Size(p);
        printf("[*] Size of the Python List = %lu\n", length);
        printf("[*] Allocated = %lu\n", p->allocated);

        while (i < length)
        {
            item = PyList_GetItem(p, i);
            printf("Element [i]: %s\n", Py_TYPE(item)->tp_name);
            i++;
        }
    }
}
