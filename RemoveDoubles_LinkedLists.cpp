// Linked Lists yay!

#include <iostream>
#include <random>
#include <unordered_map>

struct Node {
  int data = 0;         // data of the node
  Node *next = nullptr; // pointer of the next node, this is initially set to a
                        // null pointer
};

void insert(Node *&head, int data) {
  Node *newNode = new Node;
  newNode->data = data; // -> is basically (*newNode).data = data
  newNode->next = head;
  head = newNode;
}

void printList(Node *head) {
  while (head) {
    std::cout << head->data << "->";
    head = head->next;
  }
  std::cout << "end" << std::endl; // endl is endline
}

void removeDuplicates(Node *head) {
  if (head == nullptr) {
    return;
  }
  Node *currentNodePtr = head;
  while (currentNodePtr) { // if it's a null pointer break
    Node *checkDuplicateNodePtr = currentNodePtr;

    while (checkDuplicateNodePtr->next) {
      if (checkDuplicateNodePtr->next->data == currentNodePtr->data) {
        checkDuplicateNodePtr->next = checkDuplicateNodePtr->next->next;
      } else {
        checkDuplicateNodePtr = checkDuplicateNodePtr->next;
      }
    }
    currentNodePtr = currentNodePtr->next;
  }
}

int main() {

  Node *head = nullptr;
  for (int i = 0; i < 10; ++i) {
    insert(head, i);
  }

  insert(head, 5);

  printList(head);
  removeDuplicates(head);
  printList(head);

  return 0;
}
