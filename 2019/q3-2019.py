ALPHA = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")


# --------------------------
# SOLUTION BY TOMMY AND JAKE
# --------------------------
# DOCUMENTED / COMMENTED BY JAKE


def is_zero_case(prefix: str, length: int) -> bool:
    """
    Computes whether there will be any valid (block)chains for a given prefix and
    chain length. We can assume there will be no valid chains if (and only if) the
    following conditions are all true:

    The prefix contains 2 consecutive letters (not necessarily adjacent);
    The latter of these consecutive letters is not the last letter of the chain;
    And there is a letter later in the alphabet (for this chain length) than the latter
    of these 2 letters which has not already appeared before them in the prefix.

    If these conditions are all true, for any combination of letters following this
    prefix, there will be a guaranteed sequence of 3 or more consecutive letters.
    """
  
    seen = []
    for index, char in enumerate(prefix):
        seen.append(char)
        for laterChar in prefix[index+1:]:
            # test the 3 above conditions
            if ord(laterChar) > ord(char) and\
              laterChar != ALPHA[length-1] and\
              any(nextChar not in seen
                  for nextChar in ALPHA[ALPHA.index(laterChar)+1:]):
                return True
            
    return False


def generate_layer(layer_size: int) -> list[int]:
    """
    Recursively calculates the number of combinations for each prefix consisting of a
    single letter (by following the observed addition sequence pattern) for all valid
    (block)chains of the given length (layer).

    The core patterns operate as follows (just trust this, cannot fully explain):

    The number of combinations beginning with the first letter will always be 1;
    
    The number of combinations beginning with either of the last 2 letters will always
    be the same;
    
    The number of combinations always ascends between each consecutive single letter
    prefix in any layer;
    
    The differences between the number of combinations for each single letter prefix in
    any layer ARE the number of combinations for each single letter prefix for the
    previous layer (in the same order);
    
    And for multi-letter prefixes, assuming they have at least one valid chain, the
    number of valid chains is simply the number of valid chains for the final letter
    of the prefix in the layer with the chain length as if you were ignoring the rest of
    the prefix (e.g. for "5 EBA", we look at the number of valid chains beginning with
    "A" in the layer with chain length 3, as there are 2 other letters in the prefix,
    which results in the correct answer of 1 valid chain (following the first pattern)).

    The penultimate pattern is the most crucial. It means we can mathematically
    calculate the number of combinations for any layer by applying the idea in reverse
    (starting with the chains of length 1, or the smallest layer). This way, we avoid
    ever actually generating any chains to find the number of valid combinations.

    Other interesting patterns can be observed which may help to explain the above or
    improve this solution in future, such as how when adding a new later letter to any
    layer, the resulting chains will always be valid when placing it in the 1st and 2nd
    place of all the original valid chains, but are irrelevant to this solution for the
    time being.
    """
  
    if layer_size <= 1:
        # base recursion case
        return [1]

    prev_layer = generate_layer(layer_size - 1)
    layer, total = [], 0

    for i in range(layer_size):
        if len(prev_layer) > i:
            # whilst the letters of the previous layer are present in this layer, we
            # can increment the running total with their number of combinations in    
            # accordance with the penultimate pattern
            total += prev_layer[i]
        # this way, the final total will appear in the layer twice at the end, in
        # accordance with the 2nd pattern
        layer.append(total)

    return layer


def count_chains(prefix: str, length: int) -> int:
    """
    Computes the number of valid (block)chains of a given length with the given prefix.
    Does not assume that any given prefix will have at least one valid chain (can return
    0), including for prefixes that are the length of a chain.
    
    This is done using consistent patterns observed through manual inspection of the
    number of valid chains for different lengths and prefixes (difficult to
    conclusively prove their validity, but they work for all tried cases), hence
    completely avoiding actually generating any chains. Detailed "explanations" of these
    patterns are in the documentation of the generate_layer function above.
    """
  
    if len(prefix) == length:
        # "prefix" is a blockchain, so just check validity
        return 0 if is_zero_case(prefix, length) else 1
    elif len(prefix) == 0:
        # no prefix, so total number of valid combinations
        return sum(generate_layer(length))
    elif len(prefix) > 1 and is_zero_case(prefix, length):
        # zero case check is redundant for single letter prefixes
        # as a single letter will always fail the first zero condition
        return 0

    # as observed, only the final letter of a given prefix is relevant
    # we can effectively traverse the layers backwards by simply calculating
    # only the layer we need, and then returning the number of combinations
    # for this final letter in that layer (or the last letter in that layer
    # if the final letter isn't present)
    layer_size = length - len(prefix) + 1
    char_index = ALPHA.index(prefix[-1])
    layer = generate_layer(layer_size)

    return layer[min(char_index, len(layer) - 1)]


inputLength, inputPrefix = input().split()
print(count_chains(inputPrefix, int(inputLength)))
