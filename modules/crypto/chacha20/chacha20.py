# ChaCha20 — Full Implementation
# Reference: RFC 8439 https://datatracker.ietf.org/doc/html/rfc8439

MAGIC_CONSTANTS = [0x61707865, 0x3320646E, 0x79622D32, 0x6B206574]


def chacha20_init_state(key: bytes, counter: int, nonce: bytes) -> list:
    """
    Build the initial 16-word ChaCha20 state matrix.

    Parameters
    ----------
    key     : 32-byte (256-bit) secret key.
    counter : 32-bit block counter.
    nonce   : 12-byte (96-bit) nonce.

    Returns
    -------
    List of 16 integers (32-bit words).
    Layout: [constants(0-3), key(4-11), counter(12), nonce(13-15)]
    """
    assert len(key) == 32, f"Key must be 32 bytes, got {len(key)}"
    assert len(nonce) == 12, f"Nonce must be 12 bytes, got {len(nonce)}"

    state = list(MAGIC_CONSTANTS)

    for i in range(8):
        state.append(int.from_bytes(key[i * 4 : i * 4 + 4], "little"))

    state.append(counter)

    for i in range(3):
        state.append(int.from_bytes(nonce[i * 4 : i * 4 + 4], "little"))

    return state


def serialize_state(state: list) -> bytes:
    """
    Serialize a 16-word state list into a 64-byte little-endian byte string.

    Parameters
    ----------
    state : List of 16 integers (32-bit words).

    Returns
    -------
    64-byte keystream block.
    """
    result = b""
    for word in state:
        result += word.to_bytes(4, "little")
    return result


def rotate_left_32(value: int, n: int) -> int:
    """
    Circular left-rotation of a 32-bit word by n positions.

    Parameters
    ----------
    value : 32-bit input word.
    n     : Number of positions to rotate left.

    Returns
    -------
    32-bit rotated word.
    """
    return ((value << n) | (value >> (32 - n))) & 0xffffffff


def quarter_round(a: int, b: int, c: int, d: int) -> tuple:
    """
    Apply the ChaCha20 quarter round to four 32-bit words (RFC 8439 ss.2.1).

    Parameters
    ----------
    a, b, c, d : Four 32-bit input words.

    Returns
    -------
    Tuple (a, b, c, d) of four 32-bit output words.
    """
    a = (a + b) & 0xffffffff; d = d ^ a; d = rotate_left_32(d, 16)
    c = (c + d) & 0xffffffff; b = b ^ c; b = rotate_left_32(b, 12)
    a = (a + b) & 0xffffffff; d = d ^ a; d = rotate_left_32(d, 8)
    c = (c + d) & 0xffffffff; b = b ^ c; b = rotate_left_32(b, 7)
    return a, b, c, d


def double_round(state: list) -> list:
    """
    Apply one ChaCha20 double round (column round + diagonal round) in place.

    Parameters
    ----------
    state : Mutable list of 16 32-bit words.

    Returns
    -------
    The same list after applying both rounds.
    """
    # Column round
    state[0],  state[4],  state[8],  state[12] = quarter_round(state[0],  state[4],  state[8],  state[12])
    state[1],  state[5],  state[9],  state[13] = quarter_round(state[1],  state[5],  state[9],  state[13])
    state[2],  state[6],  state[10], state[14] = quarter_round(state[2],  state[6],  state[10], state[14])
    state[3],  state[7],  state[11], state[15] = quarter_round(state[3],  state[7],  state[11], state[15])

    # Diagonal round
    state[0],  state[5],  state[10], state[15] = quarter_round(state[0],  state[5],  state[10], state[15])
    state[1],  state[6],  state[11], state[12] = quarter_round(state[1],  state[6],  state[11], state[12])
    state[2],  state[7],  state[8],  state[13] = quarter_round(state[2],  state[7],  state[8],  state[13])
    state[3],  state[4],  state[9],  state[14] = quarter_round(state[3],  state[4],  state[9],  state[14])

    return state


def chacha20_block(key: bytes, nonce: bytes, counter: int) -> bytes:
    """
    Generate one 64-byte ChaCha20 keystream block (RFC 8439 ss.2.3).

    Parameters
    ----------
    key     : 32-byte secret key.
    nonce   : 12-byte nonce.
    counter : 32-bit block counter.

    Returns
    -------
    64-byte keystream block.
    """
    initial = chacha20_init_state(key, counter, nonce)
    working = list(initial)

    for _ in range(10):
        double_round(working)

    working = [(working[i] + initial[i]) & 0xffffffff for i in range(16)]
    return serialize_state(working)


def chacha20_encrypt(plaintext: bytes, key: bytes, nonce: bytes, counter: int) -> bytes:
    """
    Encrypt an arbitrary-length message with ChaCha20 (RFC 8439 ss.2.4).

    Parameters
    ----------
    plaintext : Message of any length (bytes).
    key       : 32-byte secret key.
    nonce     : 12-byte nonce.
    counter   : Initial block counter.

    Returns
    -------
    Ciphertext of the same length as plaintext.
    """
    ct = b""
    for i in range((len(plaintext) + 63) // 64):
        chunk = plaintext[i * 64 : (i + 1) * 64]
        ks = chacha20_block(key, nonce, counter + i)
        ct += bytes(p ^ k for p, k in zip(chunk, ks))
    return ct


def chacha20_decrypt(ciphertext: bytes, key: bytes, nonce: bytes, counter: int) -> bytes:
    """
    Decrypt a ChaCha20 ciphertext.

    ChaCha20 is a stream cipher — decryption is identical to encryption.

    Parameters
    ----------
    ciphertext : Ciphertext of any length (bytes).
    key        : 32-byte secret key.
    nonce      : 12-byte nonce used during encryption.
    counter    : Initial block counter used during encryption.

    Returns
    -------
    Recovered plaintext.
    """
    return chacha20_encrypt(ciphertext, key, nonce, counter)
