import math

def rad(x):
    return x * math.PI / 180;


def checkDistanceReal(userLocation, coordanites):
    R =  6378137
    dLat = rad(coordanites[0] - userLocation[0])
    dLong = rad(coordanites[1] - userLocation[1])
    a = math.sin(dLat / 2) * math.sin(dLat / 2) + math.cos(rad(userLocation.latitude)) * \
                                                  math.cos(rad(userLocation[0])) * \
                                                  math.sin(dLong / 2) * math.sin(dLong / 2);


            double a =
            double c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
            double d = R * c;

            if (d < 10) {
                return count;
            }
            count++;
        }

        return -1;
    }