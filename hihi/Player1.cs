using UnityEngine;
using UnityEngine.UI;

public class Player1 : MonoBehaviour
{
    [SerializeField] private float moveSpeed = 1f;

    private Rigidbody2D rb;

    private float moveX, moveY;

    public static Player1 instance;

    [SerializeField] private Slider sliderHP;

    [SerializeField] private float maxHP;

    [SerializeField] private float currentHP;


    [SerializeField] private bool isHittedFromDamageZone = false;

    [SerializeField] private float timeCooldown = 2f;

    [SerializeField] private float currentTimeCooldown = 0f;

    [SerializeField] private GameObject bulletPre;

    [SerializeField] private Transform posShooting;

    private Animator animator;

    private Vector3 moveVelocity;

    private Vector2 dirShooting;

  //  private float lastMoveX , lastMoveY;
    private void Awake()
    {
        rb = GetComponent<Rigidbody2D>();
        animator = GetComponent<Animator>();
        if (instance != null && instance != this)
        {
            Destroy(gameObject);
            return;
        }
        else
        {
            instance = this;
        }
        currentHP = maxHP;
        sliderHP.maxValue = maxHP;
        sliderHP.value = currentHP;
    }

    void Update()
    {
        moveX = Input.GetAxis("Horizontal") * moveSpeed;

        moveY = Input.GetAxis("Vertical") * moveSpeed;

        moveVelocity = new Vector3(moveX, moveY, 0f);
        animator.SetFloat("Speed", moveVelocity.magnitude);

        if(moveVelocity.magnitude > 0.01f)
        {
            if(Mathf.Abs(moveX) > Mathf.Abs(moveY))
            {
                animator.SetFloat("Look X", moveX > 0 ? 1 : -1);
                animator.SetFloat("Look Y", 0);
                dirShooting = moveX > 0 ? Vector2.right : Vector2.left;
            }
            else
            {
                animator.SetFloat("Look Y", moveY > 0 ? 1 : -1);
                animator.SetFloat("Look X", 0);
                dirShooting = moveY > 0 ? Vector2.up : Vector2.down;
            }
        }
        Cooldown();
        Attack();
    }

    private void Cooldown()
    {
        if(isHittedFromDamageZone)
        {
            currentTimeCooldown -= Time.deltaTime;
            if(currentTimeCooldown <= 0f)
            {
                currentTimeCooldown = timeCooldown ;
                isHittedFromDamageZone = false ;
            }
        }
    }

    private void FixedUpdate()
    {
        rb.linearVelocity = moveVelocity;
    }
  

    public void TakeDamage(float damage)
    {
        if (isHittedFromDamageZone == false)
        {
            currentHP = Mathf.Clamp(currentHP + damage, 0, maxHP);
            sliderHP.value = currentHP;
            isHittedFromDamageZone = true;
            animator.SetTrigger("Hit");
        }
    }

    private GameObject a; 
    private void Attack()
    {
        if (Input.GetKeyDown(KeyCode.Mouse0))
        {
            animator.SetTrigger("Attach");
            a = Instantiate(bulletPre, rb.position + Vector2.up * 0.5f, Quaternion.identity);     
            if( a  != null)
            {         
                a.GetComponent<BanTinh>().SetDir(dirShooting);
            }
        }
    }
}
