import sys
import math

def read_junction_boxes(filename, n_closest_boxes):

    with open(filename, 'r') as fh:
        lines = [line.rstrip('\n') for line in fh]

    junction_boxes = []
    for line in lines:
        x,y,z = line.split(',')
        junction_boxes.append((int(x), int(y), int(z)))

    num_junction_boxes = len(junction_boxes)
    print(f"Number of junction boxes {num_junction_boxes}")

    distance_matrix = []
    for pointA_index, pointA in enumerate(junction_boxes):
        for pointB_index, pointB in enumerate(junction_boxes[pointA_index:]):
            if pointA_index == pointA_index+pointB_index:
                continue
            dist = math.sqrt( (pointB[0]-pointA[0])**2 + (pointB[1]-pointA[1])**2 + (pointB[2]-pointA[2])**2 )
            # distance_matrix.append( (dist, pointA, pointB) )
            distance_matrix.append( (dist, pointA_index, pointA_index+pointB_index) )

    sorted_distance_matrix = sorted(distance_matrix)

    circuits = [{sorted_distance_matrix[0][1],sorted_distance_matrix[0][2]}]

    # for dist, boxA, boxB in sorted_distance_matrix[1:]:
    # for count, (dist, boxA, boxB) in enumerate(sorted_distance_matrix[1:n_closest_boxes]):
    # keep track of un/connected boxes
    unconnected_boxes = set(range(num_junction_boxes))
    # remove the initial two boxes
    unconnected_boxes.remove(sorted_distance_matrix[0][1])
    unconnected_boxes.remove(sorted_distance_matrix[0][2])
    for dist, boxA, boxB in sorted_distance_matrix[1:n_closest_boxes]:
        new_pair = {boxA, boxB}
        # print(f"{unconnected_boxes}: {new_pair}")
        # if not unconnected_boxes.isdisjoint(new_pair):
        if new_pair - unconnected_boxes:
            # print("Pair has at least one connected box")
            continue
        found_circuit = False
        for circuit in circuits:
            if not circuit.isdisjoint(new_pair):
                found_circuit = True
                circuit |= new_pair
                break

        if not found_circuit:
            circuits.append(new_pair)

        # remove these now connected boxes
        unconnected_boxes.remove(boxA)
        unconnected_boxes.remove(boxB)

    return circuits


if __name__ == "__main__":
    file = sys.argv[1]
    if len(sys.argv) == 3:
        n_closest_boxes = int(sys.argv[2])+1
    else:
        n_closest_boxes = None

    circuits = read_junction_boxes(file, n_closest_boxes)
    len_circuits = [len(c) for c in circuits]
    print(f"The sizes of each circuit are {len_circuits}")
    top_three_circuit_lengths = sorted(len_circuits, reverse=True)[:3]
    print(f"The three largest circuits are {top_three_circuit_lengths}")
    product_of_top_three_circuits = math.prod(top_three_circuit_lengths)
    print(f"The product of the three largest circuits sizes is {product_of_top_three_circuits}")
