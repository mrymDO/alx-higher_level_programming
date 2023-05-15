#include <Python.h>

/**
 * print_python_list_info -  prints basic info about Python lists
 * @p: a pointer to the list object from which we want to retrive information. it's type is 'PyObject*'
 * Return: void
 */

void print_python_list_info(PyObject *p)
{
	ssize_t i, size, allocated_size;
	PyObject *items;

	size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);

	if (PyList_Check(p))
		allocated_size = ((PyListObject *)p)->allocated;
	printf("[*] Allocated = %ld\n", allocated_size);

	for (i = 0; i < size; i++)
	{
		items = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(items)->tp_name);
		
	}
}
