import base64
import six
import uuid

name = "d1f91e09-4f15-4110-9ae2-9c26ac6fbffb"
uuid_str = name.replace("-", "")
vol_uuid = uuid.UUID('urn:uuid:%s' % uuid_str)
vol_encoded = base64.b64encode(vol_uuid.bytes)
if six.PY3:
    vol_encoded = vol_encoded.decode('ascii')
vol_encoded = vol_encoded.replace('=', '')

# + is not a valid character for DotHill
vol_encoded = vol_encoded.replace('+', '.')
# since we use http URLs to send paramters, '/' is not an acceptable
# parameter
vol_encoded = vol_encoded.replace('/', '_')
# NOTE:we limit the size to 20 characters since the array
# doesn't support more than that for now. Duplicates should happen very
# rarely.
# We return 19 chars here because the _get_{vol,snap}_name functions
# prepend a character
print vol_encoded[:19]
