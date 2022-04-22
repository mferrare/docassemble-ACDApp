import base64
import json
import lzma
def serialise_and_encode(ACDData):
    """
    Dumps data into JSON, compresses and encodes for inclusion in 
    a URL
    """
    j = json.dumps(ACDData)
    bj = j.encode('utf-8')
    lz = lzma.compress(bj)
    b = base64.urlsafe_b64encode(lz)
    return b

def decode_and_return_data(ACDEncodedData):
    """
    Decodes the data that should have encided using serialise_and_encode()
    - uncompresses
    - converts UTF-8 to text
    - converts JSON to python object
    - returns the object
    """
    u = base64.urlsafe_b64decode(ACDEncodedData)
    d = lzma.decompress(u)
    a = d.decode('utf-8')
    return a

