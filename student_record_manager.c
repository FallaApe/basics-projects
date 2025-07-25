#include <stdio.h>
#include <stdlib.h>

int main() {
    int option;
    char name[50];
    int classs;
    float marks;

    while (1) {
        // display menu
        printf("\nChoose an option:\n");
        printf("1) Add student details\n");
        printf("2) View student details\n");
        printf("3) Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &option);

        if (option == 1) {
            // add student details
            printf("\nEnter name of student: ");
            scanf("%s", name);  // note: this won't accept spaces. use fgets() for full names

            printf("Enter class: ");
            scanf("%d", &classs);

            printf("Enter percentage: ");
            scanf("%f", &marks);

            // open file in append mode
            FILE *fptr = fopen("student.txt", "a");
            if (fptr == NULL) {
                printf("Error opening file.\n");
                continue;
            }

            // write to file
            fprintf(fptr, "%s %d %.2f\n", name, classs, marks);
            printf("Student record added successfully.\n");

            fclose(fptr);
        }
        else if (option == 2) {
            // view student details
            FILE *fptr = fopen("student.txt", "r");
            if (fptr == NULL) {
                printf("File not found or empty.\n");
                continue;
            }

            printf("\n--- Student Records ---\n\n");

            // read and display each record from the file
            while (fscanf(fptr, "%s %d %f", name, &classs, &marks) == 3) {
                printf("Name: %s\tClass: %d\tPercentage: %.2f\n", name, classs, marks);
            }

            fclose(fptr);
        }
        else if (option == 3) {
            // exit the program
            printf("Exiting program. Goodbye!\n");
            exit(0);
        }
        else {
            // invalid input
            printf("Invalid option, please try again.\n");
        }
    }

    return 0;
}
