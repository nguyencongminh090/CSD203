#include <iostream>
#include <list>
#include <utility>

struct Node {
    int          data;
    struct Node* next;
    Node(int d, Node* n=nullptr) : data(d), next(n) {}
};

class LinkedList {
    public:
        Node* head = nullptr;
        Node* tail = nullptr;
    
    bool is_empty() {
        return this->head == nullptr;
    }

    void push_front(int x) {
        Node* new_node = new Node(x, nullptr);
        if (is_empty()) {
            this->head = new_node;
            this->tail = new_node;
        } else {
            new_node->next = this->head;
            this->head = new_node;
        }
    }
    void push_back(int x) {
        Node* new_node = new Node(x, nullptr);
        if (is_empty()) {
            this->head = new_node;
            this->tail = new_node;
        } else {
            this->tail->next = new_node;
            this->tail       = new_node;
        }
    }
    void remove_head() {
        if (is_empty()) {
            return;
        } else if (this->head == this->tail) {
            delete this->head;
            this->head = this->tail = nullptr;
        } else {
            Node* temp = this->head;
            this->head = this->head->next;
            delete temp;
        }
    }
    void remove_tail() {
        if (is_empty()) {
            return;
        } else if (this->head == this->tail) {
            delete this->head;
            this->head = this->tail = nullptr;
        } else {
            Node* pcurrent = this->head;
            while (pcurrent->next != this->tail) {
                pcurrent = pcurrent->next;
            }
            delete this->tail;
            pcurrent->next = nullptr;
        }
    }
    void remove_index(int index=0) {
        if (is_empty()) {
            return;
        }
        if (index == 0) {
            remove_head();
        }
        Node* pcurrent = this->head;
        int   pindex   = 0;
        while (pcurrent->next != nullptr && pindex + 1 < index) {
            pcurrent = pcurrent->next;
            pindex++;
        }
        Node* target = pcurrent->next;
        if (target == nullptr) return;
        
        if (pcurrent->next == this->tail) {
            this->tail = pcurrent;
        }
        pcurrent->next = target->next;
        delete target;
    }
    void update_node(int data, int index) {
        if (is_empty()) {
            return;
        }
        int   pindex   = 0;
        Node* pcurrent = this->head;
        while (pcurrent && pindex < index) {
            pcurrent = pcurrent->next;
            pindex ++;
        }
        if (pcurrent) {
            pcurrent->data = data;
        }
    }
    int length() {
        int c = 0;
        Node *pcurrent = this->head;
        while (pcurrent != nullptr) {
            pcurrent = pcurrent->next;
            c++;
        }
        return c;
    }
    void travesal() {
        Node* pcurrent = this->head;
        std::cout << "--Travesal--" << std::endl;
        while (pcurrent != nullptr) {
            Node* next = pcurrent->next;
            std::cout << pcurrent->data << " -> ";
            pcurrent = next;
        }
        std::cout << std::endl;
    };    
    ~LinkedList() {
        Node* pcurrent = this->head;
        while (pcurrent != nullptr) {
            Node* next = pcurrent->next;
            delete pcurrent;
            pcurrent   = next;
        }
    }
};

int main() {
    // std::list<int> linked_list;
    // linked_list.push_back(0);
    // linked_list.push_front(5);
    // linked_list.push_back(10);
    // linked_list.push_front(20);
    // linked_list.push_front(25);
    // for (const int& element : linked_list) {
    //     std::cout  << element << " -> ";
    // 

    LinkedList my_linked_list;
    my_linked_list.push_back(0);
    my_linked_list.push_front(5);
    my_linked_list.push_back(10);
    my_linked_list.push_front(20);
    my_linked_list.push_front(25);
    my_linked_list.remove_head();
    my_linked_list.remove_tail();
    my_linked_list.remove_index(2);
    my_linked_list.update_node(3, 1);
    my_linked_list.travesal();
    std::cout << "Length: " << my_linked_list.length() << std::endl;
}