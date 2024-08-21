import java.io.*;
import java.util.*;

public class Main {

    private  static ArrayList<Integer>[] A;
    private  static  boolean[] visited;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        //입력
        int N = Integer.parseInt(st.nextToken()); // 노드
        int M = Integer.parseInt(st.nextToken()); //에지
        int V = Integer.parseInt(st.nextToken()); //시작노드

        A = new ArrayList[N + 1];
        visited = new boolean[N + 1];
        int a = 0;
        int b = 0;

        //초기화
        for(int i = 1 ; i < N + 1 ; i++){ //노드 갯수만큼 반복
            A[i] = new ArrayList<Integer>();
        }

        //
        for(int i = 1 ; i < M+1 ; i ++){ //에지 갯수만큼 반복
            st = new StringTokenizer(br.readLine());
            a =  Integer.parseInt(st.nextToken());
            b = Integer.parseInt(st.nextToken());

            //양쪽에 연결완료
            A[a].add(b);
            A[b].add(a);
        }

//boolean 초기화 하면 false가 기본인줄 몰랐음
                // 각 노드별 탐색시작
        //        for(int i = 1 ; i < N + 1 ; i++) {

        //            visited[i] = false; //초기화

        //        }

        //순서대비 (오름차순 정렬)
        for(int i = 1 ; i < N + 1 ; i++){
            Collections.sort(A[i]);
        }

        visited = new boolean[N+1];

// 연결요소 처럼 그래프가 여러개인 경우 이용하는 것임
//        for(int i = 1 ; i < N + 1 ; i++){

//            if(! visited[i])
                dfs(V);
//        }
        System.out.println();

        visited = new boolean[N+1];
        bfs(V);
        System.out.println();

    }

    private static void dfs(int v) {
        System.out.print(v + " ");

//        //방문확인
        if(visited[v]) return ;

//
//
//        //인접노드들의 방문체크
//        visited[v + 1] = true;
//
//
//        for(int i = 1 ; i < A.length + 1 ; i++)
//            dfs(i);
//
//        return v;
//        if(visited[v+1]) return;

        visited[v] = true;

        for(int i : A[v])
            if(!visited[i]) dfs(i);

    }

    private static void bfs(int v) {
        //큐 선언
        Queue<Integer> queue = new LinkedList<Integer>();

    //1
        //큐에 삽입 시   // 방문배열에 남기기
        queue.add(v); visited[v] = true;

    //2
        //while 쓰는 이유는 재귀함수가 아니라 queue를 쓰기 때문
        //큐가 빌 때 까지 반복
        while (!queue.isEmpty()){

    //3
            //큐에서 꺼낸다. // 방문순서 출력하
            int now_Node = queue.poll(); System.out.print(now_Node + " ");

    //4
            //꺼내느 노드의 인접노드를 탐색한다.
            for(int i : A[now_Node]){

    //5
                //인접노드가 방문하지 않았으면
                if(!visited[i]) {
                    //방문배열에 남기고
                    //큐에 넣는다./
                    queue.add(i);
                    visited[i] = true;
                }
            }
        }
    }
}
