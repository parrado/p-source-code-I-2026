#include <string>

class Person {

  public:
    int id;

public:
    std::string name;

    Person(const std::string& name, int id) : name(name), id(id) {}

    int getId() const {
        return id;
    }

    void setId(int newId) {
        id = newId;
    }
};

int main(){
    Person p("Alice", 1234);
     p.id = 5678; // Error: 'id' is private
    p.setId(5678); // Correct way to modify 'id'
    int id = p.getId(); // Correct way to access 'id'
}