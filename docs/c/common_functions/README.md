# Common functions used in C for DS & AL problems

## Memory functions
A lot of times you'll find yourself searching for some function to alocate memory dynamically, for array operations, strings, etc...
Here are some functions that can be useful:
* `void * malloc(size_t __size)` - This functions takes a size as parameter and allocates memory for the variable that is calling it, Ex:
  ```c
  int *size = malloc(sizeof(int) * 23)
  ```
  In this case 23 blocks of memory with ints are been allocated for the variable `size`.

* `void * calloc(size_t __nmemb, size_t __size)` - This functions works the same way as `malloc()`, the only difference is that it takes two arguments instead of one, and return the blocks of memory filled with 0's. Ex:
  ```c
  int *size = calloc(23, sizeof(int));
  ```

* `void free(void * __ptr)` - This function frees memory allocated by `malloc()`, `calloc()` or `realloc()`. Ex:
  ```c
  free(size);
  ```
