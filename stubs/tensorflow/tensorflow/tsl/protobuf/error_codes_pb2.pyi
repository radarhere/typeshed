"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
TODO(b/247876220): Change package and java_package once we figure out how to
migrate.
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _Code:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _CodeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_Code.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    OK: _Code.ValueType  # 0
    """Not an error; returned on success"""
    CANCELLED: _Code.ValueType  # 1
    """The operation was cancelled (typically by the caller)."""
    UNKNOWN: _Code.ValueType  # 2
    """Unknown error.  An example of where this error may be returned is
    if a Status value received from another address space belongs to
    an error-space that is not known in this address space.  Also
    errors raised by APIs that do not return enough error information
    may be converted to this error.
    """
    INVALID_ARGUMENT: _Code.ValueType  # 3
    """Client specified an invalid argument.  Note that this differs
    from FAILED_PRECONDITION.  INVALID_ARGUMENT indicates arguments
    that are problematic regardless of the state of the system
    (e.g., a malformed file name).
    """
    DEADLINE_EXCEEDED: _Code.ValueType  # 4
    """Deadline expired before operation could complete.  For operations
    that change the state of the system, this error may be returned
    even if the operation has completed successfully.  For example, a
    successful response from a server could have been delayed long
    enough for the deadline to expire.
    """
    NOT_FOUND: _Code.ValueType  # 5
    """Some requested entity (e.g., file or directory) was not found.
    For privacy reasons, this code *may* be returned when the client
    does not have the access right to the entity.
    """
    ALREADY_EXISTS: _Code.ValueType  # 6
    """Some entity that we attempted to create (e.g., file or directory)
    already exists.
    """
    PERMISSION_DENIED: _Code.ValueType  # 7
    """The caller does not have permission to execute the specified
    operation.  PERMISSION_DENIED must not be used for rejections
    caused by exhausting some resource (use RESOURCE_EXHAUSTED
    instead for those errors).  PERMISSION_DENIED must not be
    used if the caller can not be identified (use UNAUTHENTICATED
    instead for those errors).
    """
    UNAUTHENTICATED: _Code.ValueType  # 16
    """The request does not have valid authentication credentials for the
    operation.
    """
    RESOURCE_EXHAUSTED: _Code.ValueType  # 8
    """Some resource has been exhausted, perhaps a per-user quota, or
    perhaps the entire file system is out of space.
    """
    FAILED_PRECONDITION: _Code.ValueType  # 9
    """Operation was rejected because the system is not in a state
    required for the operation's execution.  For example, directory
    to be deleted may be non-empty, an rmdir operation is applied to
    a non-directory, etc.

    A litmus test that may help a service implementor in deciding
    between FAILED_PRECONDITION, ABORTED, and UNAVAILABLE:
     (a) Use UNAVAILABLE if the client can retry just the failing call.
     (b) Use ABORTED if the client should retry at a higher-level
         (e.g., restarting a read-modify-write sequence).
     (c) Use FAILED_PRECONDITION if the client should not retry until
         the system state has been explicitly fixed.  E.g., if an "rmdir"
         fails because the directory is non-empty, FAILED_PRECONDITION
         should be returned since the client should not retry unless
         they have first fixed up the directory by deleting files from it.
     (d) Use FAILED_PRECONDITION if the client performs conditional
         REST Get/Update/Delete on a resource and the resource on the
         server does not match the condition. E.g., conflicting
         read-modify-write on the same resource.
    """
    ABORTED: _Code.ValueType  # 10
    """The operation was aborted, typically due to a concurrency issue
    like sequencer check failures, transaction aborts, etc.

    See litmus test above for deciding between FAILED_PRECONDITION,
    ABORTED, and UNAVAILABLE.
    """
    OUT_OF_RANGE: _Code.ValueType  # 11
    """Operation tried to iterate past the valid input range.  E.g., seeking or
    reading past end of file.

    Unlike INVALID_ARGUMENT, this error indicates a problem that may
    be fixed if the system state changes. For example, a 32-bit file
    system will generate INVALID_ARGUMENT if asked to read at an
    offset that is not in the range [0,2^32-1], but it will generate
    OUT_OF_RANGE if asked to read from an offset past the current
    file size.

    There is a fair bit of overlap between FAILED_PRECONDITION and
    OUT_OF_RANGE.  We recommend using OUT_OF_RANGE (the more specific
    error) when it applies so that callers who are iterating through
    a space can easily look for an OUT_OF_RANGE error to detect when
    they are done.
    """
    UNIMPLEMENTED: _Code.ValueType  # 12
    """Operation is not implemented or not supported/enabled in this service."""
    INTERNAL: _Code.ValueType  # 13
    """Internal errors.  Means some invariant expected by the underlying
    system has been broken.  If you see one of these errors,
    something is very broken.
    """
    UNAVAILABLE: _Code.ValueType  # 14
    """The service is currently unavailable.  This is a most likely a
    transient condition and may be corrected by retrying with
    a backoff.

    See litmus test above for deciding between FAILED_PRECONDITION,
    ABORTED, and UNAVAILABLE.
    """
    DATA_LOSS: _Code.ValueType  # 15
    """Unrecoverable data loss or corruption."""
    DO_NOT_USE_RESERVED_FOR_FUTURE_EXPANSION_USE_DEFAULT_IN_SWITCH_INSTEAD_: _Code.ValueType  # 20
    """An extra enum entry to prevent people from writing code that
    fails to compile when a new code is added.

    Nobody should ever reference this enumeration entry. In particular,
    if you write C++ code that switches on this enumeration, add a default:
    case instead of a case that mentions this enumeration entry.

    Nobody should rely on the value (currently 20) listed here.  It
    may change in the future.
    """

class Code(_Code, metaclass=_CodeEnumTypeWrapper):
    """The canonical error codes for TensorFlow APIs.

    Warnings:

    -   Do not change any numeric assignments.
    -   Changes to this list should only be made if there is a compelling
        need that can't be satisfied in another way.  Such changes
        must be approved by at least two OWNERS.
    -   These error codes must match gRPC and protobuf error codes (except for
        DO_NOT_USE_RESERVED_FOR_FUTURE_EXPANSION_USE_DEFAULT_IN_SWITCH_INSTEAD_).

    Sometimes multiple error codes may apply.  Services should return
    the most specific error code that applies.  For example, prefer
    OUT_OF_RANGE over FAILED_PRECONDITION if both codes apply.
    Similarly prefer NOT_FOUND or ALREADY_EXISTS over FAILED_PRECONDITION.
    """

OK: Code.ValueType  # 0
"""Not an error; returned on success"""
CANCELLED: Code.ValueType  # 1
"""The operation was cancelled (typically by the caller)."""
UNKNOWN: Code.ValueType  # 2
"""Unknown error.  An example of where this error may be returned is
if a Status value received from another address space belongs to
an error-space that is not known in this address space.  Also
errors raised by APIs that do not return enough error information
may be converted to this error.
"""
INVALID_ARGUMENT: Code.ValueType  # 3
"""Client specified an invalid argument.  Note that this differs
from FAILED_PRECONDITION.  INVALID_ARGUMENT indicates arguments
that are problematic regardless of the state of the system
(e.g., a malformed file name).
"""
DEADLINE_EXCEEDED: Code.ValueType  # 4
"""Deadline expired before operation could complete.  For operations
that change the state of the system, this error may be returned
even if the operation has completed successfully.  For example, a
successful response from a server could have been delayed long
enough for the deadline to expire.
"""
NOT_FOUND: Code.ValueType  # 5
"""Some requested entity (e.g., file or directory) was not found.
For privacy reasons, this code *may* be returned when the client
does not have the access right to the entity.
"""
ALREADY_EXISTS: Code.ValueType  # 6
"""Some entity that we attempted to create (e.g., file or directory)
already exists.
"""
PERMISSION_DENIED: Code.ValueType  # 7
"""The caller does not have permission to execute the specified
operation.  PERMISSION_DENIED must not be used for rejections
caused by exhausting some resource (use RESOURCE_EXHAUSTED
instead for those errors).  PERMISSION_DENIED must not be
used if the caller can not be identified (use UNAUTHENTICATED
instead for those errors).
"""
UNAUTHENTICATED: Code.ValueType  # 16
"""The request does not have valid authentication credentials for the
operation.
"""
RESOURCE_EXHAUSTED: Code.ValueType  # 8
"""Some resource has been exhausted, perhaps a per-user quota, or
perhaps the entire file system is out of space.
"""
FAILED_PRECONDITION: Code.ValueType  # 9
"""Operation was rejected because the system is not in a state
required for the operation's execution.  For example, directory
to be deleted may be non-empty, an rmdir operation is applied to
a non-directory, etc.

A litmus test that may help a service implementor in deciding
between FAILED_PRECONDITION, ABORTED, and UNAVAILABLE:
 (a) Use UNAVAILABLE if the client can retry just the failing call.
 (b) Use ABORTED if the client should retry at a higher-level
     (e.g., restarting a read-modify-write sequence).
 (c) Use FAILED_PRECONDITION if the client should not retry until
     the system state has been explicitly fixed.  E.g., if an "rmdir"
     fails because the directory is non-empty, FAILED_PRECONDITION
     should be returned since the client should not retry unless
     they have first fixed up the directory by deleting files from it.
 (d) Use FAILED_PRECONDITION if the client performs conditional
     REST Get/Update/Delete on a resource and the resource on the
     server does not match the condition. E.g., conflicting
     read-modify-write on the same resource.
"""
ABORTED: Code.ValueType  # 10
"""The operation was aborted, typically due to a concurrency issue
like sequencer check failures, transaction aborts, etc.

See litmus test above for deciding between FAILED_PRECONDITION,
ABORTED, and UNAVAILABLE.
"""
OUT_OF_RANGE: Code.ValueType  # 11
"""Operation tried to iterate past the valid input range.  E.g., seeking or
reading past end of file.

Unlike INVALID_ARGUMENT, this error indicates a problem that may
be fixed if the system state changes. For example, a 32-bit file
system will generate INVALID_ARGUMENT if asked to read at an
offset that is not in the range [0,2^32-1], but it will generate
OUT_OF_RANGE if asked to read from an offset past the current
file size.

There is a fair bit of overlap between FAILED_PRECONDITION and
OUT_OF_RANGE.  We recommend using OUT_OF_RANGE (the more specific
error) when it applies so that callers who are iterating through
a space can easily look for an OUT_OF_RANGE error to detect when
they are done.
"""
UNIMPLEMENTED: Code.ValueType  # 12
"""Operation is not implemented or not supported/enabled in this service."""
INTERNAL: Code.ValueType  # 13
"""Internal errors.  Means some invariant expected by the underlying
system has been broken.  If you see one of these errors,
something is very broken.
"""
UNAVAILABLE: Code.ValueType  # 14
"""The service is currently unavailable.  This is a most likely a
transient condition and may be corrected by retrying with
a backoff.

See litmus test above for deciding between FAILED_PRECONDITION,
ABORTED, and UNAVAILABLE.
"""
DATA_LOSS: Code.ValueType  # 15
"""Unrecoverable data loss or corruption."""
DO_NOT_USE_RESERVED_FOR_FUTURE_EXPANSION_USE_DEFAULT_IN_SWITCH_INSTEAD_: Code.ValueType  # 20
"""An extra enum entry to prevent people from writing code that
fails to compile when a new code is added.

Nobody should ever reference this enumeration entry. In particular,
if you write C++ code that switches on this enumeration, add a default:
case instead of a case that mentions this enumeration entry.

Nobody should rely on the value (currently 20) listed here.  It
may change in the future.
"""
global___Code = Code