class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        row=[1]
        for i in range(rowIndex):
            row = [1] + [row[j - 1] + row[j] for j in range(1, len(row))] + [1]
        return row

        