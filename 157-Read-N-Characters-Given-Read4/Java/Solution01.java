/* The read4 API is defined in the parent class Reader4.
      int read4(char[] buf); */

public class Solution extends Reader4 {
    /**
    * @param buf Destination buffer
    * @param n Maximum number of characters to read
    * @return The number of characters read
    */
    public int read(char[] buf, int n) {
        char[] buffer = new char[4];
        int readBytes = 0;
        boolean eof = false;
        while (!eof && readBytes < n) {
            int size = read4(buffer);
            if (size < 4) eof = true;
            int bytes = Math.min(n - readBytes, size);
            System.arraycopy(buffer /* src */, 0 /* srcPos */,
            buf /* dest */, readBytes /* destPos */, bytes /* length */);
            readBytes += bytes;
        }
        return readBytes;
        }
}