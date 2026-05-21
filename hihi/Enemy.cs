using UnityEngine;

public class Enemy : MonoBehaviour
{

    [SerializeField] private float moveSpeed = 1f;

    [SerializeField] private Transform posA; 

    [SerializeField] private Transform posB;

    private Rigidbody2D rb;

    private Animator animator;

    private Vector2 target;

    private Vector2 firstPositionA;

    private Vector2 firstPositionB;

    private float moveX, moveY;

 

    private void Awake()
    {
        rb = GetComponent<Rigidbody2D>();
        animator= GetComponent<Animator>();
    }
    void Start()
    {
        firstPositionA = posA.position;
        firstPositionB = posB.position;
        target = firstPositionA;
    }

    void Update()
    {
        Vector2 current = rb.position;

        Vector2 direction = (target - current).normalized;

        rb.linearVelocity = direction * moveSpeed;

        if (Vector2.Distance(transform.position, target) < 0.05f)
        { 
            if (target == (Vector2)firstPositionA)
            {
                target = firstPositionB;
            }
            else
            {
                target = firstPositionA;
            }
        }

        bool isMoving = direction.x != 0 || direction.y != 0;
        
       // animator.SetBool("Running", isMoving);

        if(isMoving)
        {

            if(Mathf.Abs(direction.x) > Mathf.Abs(direction.y))
            {
                animator.SetFloat("MoveX", direction.x > 0 ? 1 : -1);
                animator.SetFloat("MoveY", 0);
            }
            else
            {
                animator.SetFloat("MoveY", direction.y > 0 ? 1 : -1);
                animator.SetFloat("MoveX", 0);
            }
        }
    }


    private void OnCollisionExit2D(Collision2D collision)
    {
        if (collision.gameObject.CompareTag("Player"))
        {
            animator.SetTrigger("Hit");
        }
    }
}
