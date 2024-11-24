#include <stdio.h>

int main() {
    int max_weight, passenger_weight;
    int total_weight = 0;
    int passenger_count = 0;

    printf("Enter the maximum weight in kg: ");
    scanf("%d", &max_weight);

    printf("Enter passenger's weight in kg: ");
    while (scanf("%d", &passenger_weight)) {
        if (total_weight + passenger_weight > max_weight) {
            break;
        }
        else if (total_weight + passenger_weight >= max_weight) {
            total_weight += passenger_weight;
            passenger_count++;
            break;
        }

        total_weight += passenger_weight;
        passenger_count++;
        

        printf("Enter passenger's weight in kg: ");
    }

    printf("The elevator can carry %d passenger(s)\n", passenger_count);

    return 0;
}
