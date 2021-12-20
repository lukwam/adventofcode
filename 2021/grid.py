"""Grid class file."""
import math


class Grid3d:
    """Grid3d class."""

    def __init__(self, cube):
        """Initialize."""
        self.cube = cube
        self.distances = None
        self.distset = None
        self.matches = []

    @classmethod
    def compare_matched_points(cls, a_points):
        diffx = []
        diffy = []
        diffz = []
        point_matches = {}
        xlock = False
        ylock = False
        zlock = False
        for a_point in a_points:
            b_points = a_points[a_point]
            b_point = max(set(b_points), key=b_points.count)
            ax, ay, az = a_point
            bx, by, bz = b_point

            dx = bx - ax
            if dx not in diffx:
                diffx.append(dx)

            dy = by - ay
            if dy not in diffy:
                diffy.append(dy)

            dz = bz - az
            if dz not in diffz:
                diffz.append(dz)

            diff = (dx, dy, dz)
            # print(f"  * Beacon {a_point}: {b_point}: {dx}, {dy}, {dz}")
            # print(f"  * Beacon {a_point} -> {b_point}")
            point_matches[a_point] = b_point
        if len(diffx) == 1:
            xlock = diffx[0] if len(diffx) == 1 else False
        if len(diffy) == 1:
            ylock = diffy[0] if len(diffy) == 1 else False
        if len(diffz) == 1:
            zlock = diffz[0] if len(diffz) == 1 else False

        if 0 in diffx and 0 in diffy and 0 in diffz:
            xlock = ylock = zlock = True

        return xlock, ylock, zlock

    @classmethod
    def get_distance(cls, a, b):
        """Return the distance between two points in a cube."""
        x1, y1, z1 = a
        x2, y2, z2 = b
        return abs(math.sqrt(
            math.pow(x2 - x1, 2)
            + math.pow(y2 - y1, 2)
            + math.pow(z2 - z1, 2)
            * 1.0
        ))

    def get_distances(self):
        """Return a dict with the distances between all points."""
        self.distances = {}
        for a in self.cube:
            for b in self.cube:
                if b == a:
                    continue
                d = self.get_distance(a, b)
                if d not in self.distances:
                    self.distances[d] = []
                for x in [a, b]:
                    if x not in self.distances[d]:
                        self.distances[d].append(x)
        self.distset = set(list(self.distances))
        return self.distances

    def get_matching_points(self, cube):
        """Find points that match between two cubes."""
        # identify possible matches
        possible_matches = self.identify_possible_matches(cube)

        # find actual matches based on the count
        xl, yl, zl = self.compare_matched_points(possible_matches)

        while xl is False or yl is False or yl is False:
            if xl is not False:
                cube.rotate_cube("u")
            elif yl is not False:
                cube.rotate_cube("r")
            elif zl is not False:
                cube.rotate_cube("c")
            else:
                cube.rotate_cube("u")
                cube.rotate_cube("r")
                cube.rotate_cube("c")

            cube.get_distances()

            # identify possible matches
            possible_matches = self.identify_possible_matches(cube)

            # find actual matches based on the count
            xl, yl, zl = self.compare_matched_points(possible_matches)

        vector = (xl, yl, zl)

        print(f"Moving cube: {vector}")
        cube.move_cube(vector)

        cube.get_distances()

        # identify possible matches
        possible_matches = self.identify_possible_matches(cube)

        # find actual matches based on the count
        xl, yl, zl = self.compare_matched_points(possible_matches)


    def identify_possible_matches(self, cube):
        dist_matches = self.distset.intersection(cube.distset)

        # identify possible matches based on distance
        a_points = {}
        for distance in sorted(dist_matches):
            a_dists = self.distances[distance]
            b_dists = cube.distances[distance]
            # print(f" * {distance}, {a_dists} / {b_dists}")

            for a_point in a_dists:
                for b_point in b_dists:
                    if a_point not in a_points:
                        a_points[a_point] = []
                    a_points[a_point].append(b_point)
        return a_points

    def move_cube(self, vector):
        vx, vy, vz = vector
        newcube = []
        for p in self.cube:
            px, py, pz = p
            n = (px-vx, py-vy, pz-vz)
            newcube.append(n)
        self.cube = newcube


    def rotate_cube(self, direction):
        """Rotate a cube once in a single direction."""
        print(f"Rotating cube: {direction}")
        newcube = []
        for p in self.cube:
            x, y, z = p
            if direction == "l":
                n = (z, y, -x)
            elif direction == "r":
                n = (-z, y, x)
            elif direction == "d":
                n = (x, z, -y)
            elif direction == "u":
                n = (x, -z, y)
            elif direction == "c":
                n = (y, -x, z)
            elif direction == "x":
                n = (-y, x, z)
            else:
                print(f"ERROR: Unknown direction: {direction}")
                continue
            newcube.append(n)
        self.cube = newcube
        return self.cube

