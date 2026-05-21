using UnityEngine;

public class BanTinh : MonoBehaviour
{
    [SerializeField] private float speed;
    private Vector3 dir;
    private Rigidbody2D rb;
    void Start()
    {
        rb = GetComponent<Rigidbody2D>();
        Destroy(gameObject, 3f);
    }

    void Update()
    {
        if (dir == Vector3.zero)
        {
            return;
        }
        rb.linearVelocity = dir.normalized * speed;
    }

    public void SetDir(Vector3 dir)
    {
        this.dir = dir.normalized;
    }

    private void OnTriggerEnter2D(Collider2D collision)
    {
        if (collision.gameObject.CompareTag("Enemy"))
        {
            print("asdasd");
            Player1.instance.HoiMau();
            Destroy(gameObject);
        }
    }
}
