class FolderNode:
    def __init__(self):
        self.subfolders = {}
        self.is_final = False

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        root = FolderNode()
        node = None
        for path in folder:
            if node:
                node.is_final = True
            node = root
            for f in path.split('/')[1:]:  # folder[i] always starts with the character '/'.
                if f not in node.subfolders:
                    node.subfolders[f] = FolderNode()
                node = node.subfolders[f]
        node.is_final = True

        result = []
        q = deque([(root, '')])
        while q:
            node, path = q.pop()
            if node.is_final:
                result.append(path)
                continue
            for subfolder, child_node in node.subfolders.items():
                q.appendleft((child_node, path + '/' + subfolder))

        return result
