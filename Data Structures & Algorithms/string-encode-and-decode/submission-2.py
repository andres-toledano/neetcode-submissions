class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for word in strs:
            result += f"{len(word)}#{word}"

        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i

            # Buscar el # que separa longitud de contenido
            while s[j] != "#":
                j += 1

            n = int(s[i:j])

            # El string empieza después del #
            j += 1

            result.append(s[j:j+n])

            # Saltamos el string que acabamos de leer
            i = j + n

        return result
