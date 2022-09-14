# global
from typing import Union, Optional

# local
import ivy
from ivy.func_wrapper import (
    to_native_arrays_and_back,
    handle_out_argument,
    handle_nestable,
)
from ivy.exceptions import handle_exceptions


# Array API Standard #
# -------------------#


@to_native_arrays_and_back
@handle_out_argument
@handle_nestable
@handle_exceptions
def argsort(
    x: Union[ivy.Array, ivy.NativeArray],
    /,
    *,
    axis: int = -1,
    descending: bool = False,
    stable: bool = True,
    out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """Returns the indices that sort an array ``x`` along a specified axis.

    Parameters
    ----------
    x
        input array.
    axis
        axis along which to sort. If set to ``-1``, the function must sort along the
        last axis. Default: ``-1``.
    descending
        sort order. If ``True``, the returned indices sort ``x`` in descending order
        (by value). If ``False``, the returned indices sort ``x`` in ascending order
        (by value). Default: ``False``.
    stable
        sort stability. If ``True``, the returned indices must maintain the relative
        order of ``x`` values which compare as equal. If ``False``, the returned indices
        may or may not maintain the relative order of ``x`` values which compare as
        equal (i.e., the relative order of ``x`` values which compare as equal is
        implementation-dependent). Default: ``True``.
    out
        optional output array, for writing the result to. It must have the same shape
        as ``x``.

    Returns
    -------
    ret
        an array of indices. The returned array must have the same shape as ``x``. The
        returned array must have the default array index data type.

    This method conforms to the `Array API Standard
    <https://data-apis.org/array-api/latest/>`_. This docstring is an extension of the
    `docstring <https://data-apis.org/array-api/latest/API_specification/generated/signatures.sorting_functions.argsort.html>`_ # noqa
    in the standard. The descriptions above assume an array input for simplicity, but
    the method also accepts :code:`ivy.Container` instances in place of
    :code:`ivy.Array` or :code:`ivy.NativeArray` instances, as shown in the type hints
    and also the examples below.

    Examples
    --------
    With: code:`ivy.Array` input:

    >>> x = ivy.array([3,1,2])
    >>> y = ivy.argsort(x)
    >>> print(y)
    ivy.array([1,2,0])

    >>> x = ivy.array([[1.5, 3.2], [2.3, 2.3]])
    >>> ivy.argsort(x, axis=0, descending=True, stable=False, out=x)
    >>> print(x)
    ivy.array([[1, 0], [0, 1]])

    >>> x = ivy.array([[[1,3], [3,2]], [[2,4], [2,0]]])
    >>> y = ivy.argsort(x, axis=1, descending=False, stable=True)
    >>> print(y)
    ivy.array([[[0, 1], [1, 0]], [[0, 1], [1, 0]]])

    With :code:`ivy.Container` input:

    >>> x = ivy.Container(a=ivy.array([5,1,3]), b=ivy.array([[0, 3], [3, 2]]))
    >>> y = ivy.argsort(x)
    >>> print(y)
    {
        a: ivy.array([1, 2, 0]),
        b: ivy.array([[0, 1], [1, 0]])
    }
    """
    return ivy.current_backend(x).argsort(
        x, axis=axis, descending=descending, stable=stable, out=out
    )


@to_native_arrays_and_back
@handle_out_argument
@handle_nestable
@handle_exceptions
def sort(
    x: Union[ivy.Array, ivy.NativeArray],
    /,
    *,
    axis: int = -1,
    descending: bool = False,
    stable: bool = True,
    out: Optional[Union[ivy.Array, ivy.NativeArray]] = None,
) -> ivy.Array:
    """Returns a sorted copy of an array.

    Parameters
    ----------
    x
        input array
    axis
        axis along which to sort. If set to ``-1``, the function must sort along the
        last axis. Default: ``-1``.
    descending
        direction  The direction in which to sort the values
    stable
        sort stability. If ``True``,
        the returned indices must maintain the relative order of ``x`` values which
        compare as equal. If ``False``, the returned indices may or may not maintain the
        relative order of ``x`` values which compare as equal (i.e., the relative order
        of ``x`` values which compare as equal is implementation-dependent).
        Default: ``True``.
    out
        optional output array, for writing the result to. It must have the same shape
        as ``x``.

    Returns
    -------
    ret
        An array with the same dtype and shape as ``x``, with the elements sorted
        along the given `axis`.


    This method conforms to the `Array API Standard
    <https://data-apis.org/array-api/latest/>`_. This docstring is an extension of the
    `docstring <https://data-apis.org/array-api/latest/API_specification/generated/signatures.sorting_functions.sort.html>`_ # noqa
    in the standard. The descriptions above assume an array input for simplicity, but
    the method also accepts :code:`ivy.Container` instances in place of
    :code:`ivy.Array` or :code:`ivy.NativeArray` instances, as shown in the type hints
    and also the examples below.


    Examples
    --------
    With :code:`ivy.Array` input:

    >>> x = ivy.array([7, 8, 6])
    >>> y = ivy.sort(x)
    >>> print(y)
    ivy.array([6, 7, 8])

    >>> x = ivy.array([[[8.9,0], [19,5]],[[6,0.3], [19,0.5]]])
    >>> y = ivy.sort(x, axis=1, descending=True, stable=False)
    >>> print(y)
    ivy.array([[[19. ,  5. ],[ 8.9,  0. ]],[[19. ,  0.5],[ 6. ,  0.3]]])

    >>> x = ivy.array([1.5, 3.2, 0.7, 2.5])
    >>> y = ivy.zeros(5)
    >>> ivy.sort(x, descending=True, stable=False, out=y)
    >>> print(y)
    ivy.array([3.2, 2.5, 1.5, 0.7])


    >>> x = ivy.array([[1.1, 2.2, 3.3],[-4.4, -5.5, -6.6]])
    >>> ivy.sort(x, out=x)
    >>> print(x)
    ivy.array([[ 1.1,  2.2,  3.3],
        [-6.6, -5.5, -4.4]])

    With :code:`ivy.NativeArray` input:

    >>> x = ivy.native_array([[[8.9, 0], [19, 5]],[[6, 0.3], [19, 0.5]]])
    >>> y = ivy.sort(x, descending=True)
    >>> print(y)
    ivy.array([[[ 8.9,  0.],[19. ,  5. ]],[[ 6. ,  0.3 ],[19. ,  0.5]]])

    With :code:`ivy.Container` input:

    >>> x = ivy.Container(a=ivy.array([8, 6, 6]),b=ivy.array([[9, 0.7], [0.4, 0]]))
    >>> y = ivy.sort(x, descending=True)
    >>> print(y)
    {
        a: ivy.array([8, 6, 6]),
        b: ivy.array([[9., 0.7], [0.4, 0.]])
    }

    >>> x = ivy.Container(a=ivy.array([3, 0.7, 1]),b=ivy.array([[4, 0.9], [0.6, 0.2]]))
    >>> y = ivy.sort(x, descending=False, stable=False)
    >>> print(y)
    {
        a: ivy.array([0.7, 1., 3.]),
        b: ivy.array([[0.9, 4.], [0.2, 0.6]])
    }

    """
    return ivy.current_backend(x).sort(
        x, axis=axis, descending=descending, stable=stable, out=out
    )


# Extra #
# ------#


@to_native_arrays_and_back
@handle_out_argument
@handle_nestable
@handle_exceptions
def searchsorted(
    x: Union[ivy.Array, ivy.NativeArray],
    v: Union[ivy.Array, ivy.NativeArray],
    /,
    *,
    side="left",
    sorter=None,
    out: Optional[ivy.Array] = None,
) -> ivy.Array:
    """Returns the indices of the inserted elements in a sorted array.

    Parameters
    ----------
    x
        input array
    v
        specific elements to insert in array x1
    side
        The specific elements' index is at the 'left' side or
        'right' side in the sorted array x1. If the side is 'left', the
        index of the first suitable location located is given. If
        'right', return the last such index.
    out
        optional output array, for writing the result to.

    Returns
    -------
    ret
         An array of insertion points.

    Examples
    --------
    With :code:`ivy.Array` input:

    >>> x1 = ivy.array([2,1,0])
    >>> x2 = ivy.array([1])
    >>> y  = ivy.searchsorted(x1,x2)
    >>> print(y)
    ivy.array([0])

    >>> x1 = ivy.array([1,0,3,2])
    >>> x2 = ivy.array([3])
    >>> y  = ivy.searchsorted(x1, x2, side='right')
    >>> print(y)
    ivy.array([4])

    >>> x1 = ivy.array([2,0,1,3])
    >>> x2 = ivy.array([3,1,9])
    >>> y  = ivy.searchsorted(x1, x2, side='left')
    >>> print(y)
    ivy.array([3,2,4])
    """
    return ivy.current_backend(x, v).searchsorted(
        x, v, side=side, sorter=sorter, out=out
    )
