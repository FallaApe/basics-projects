#include <stdio.h>
#include <stdlib.h>

// structure to store student details
struct structure1 {
    int age;
    int class;
};

int main() {
    int option, option2;
    
    while (1) {
        printf("1) Enter details\n");
        printf("2) Exit\n");
        printf("Enter option: ");
        scanf("%d", &option);

        if (option == 1) {
            printf("How many students' data do you want to enter (max 5): ");
            scanf("%d", &option2);

            if (option2 > 5) {
                printf("You can only enter up to 5 students.\n");
                continue;
            }

            struct structure1 s[5]; // array of structures

            for (int i = 0; i < option2; i++) {
                printf("Enter age and class for student %d: ", i + 1);
                scanf("%d %d", &s[i].age, &s[i].class); // store directly in struct
            }

            printf("\nStudent Details:\n");
            for (int i = 0; i < option2; i++) {
                printf("Age: %d\tClass: %d\n", s[i].age, s[i].class);
            }
        }
        else if (option == 2) {
            printf("Bye bye\n");
            exit(0);
        }
        else {
            printf("Error, try again\n");
        }
    }

    return 0;
}
